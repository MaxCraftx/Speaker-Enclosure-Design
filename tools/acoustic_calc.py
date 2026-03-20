"""
Acoustic Calculator Toolkit for Speaker Enclosure Design.
Hardcoded into the Speaker-Enclosure-Design project environment.

Usage:
    from tools.acoustic_calc import PortedEnclosure, port_resonance, port_air_velocity

Based on Thiele-Small modeling for ported (bass-reflex) enclosures.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import os

# ─── Constants ───
SPEED_OF_SOUND = 343.0  # m/s at 20°C
AIR_DENSITY = 1.204     # kg/m³ at 20°C


def port_resonance(volume_litres: float, port_diameter_mm: float, port_length_mm: float) -> float:
    """
    Calculate the Helmholtz resonance frequency of a ported enclosure.
    
    Args:
        volume_litres: Internal air volume of the enclosure in litres
        port_diameter_mm: Inner diameter of the port tube in mm
        port_length_mm: Effective length of the port tube in mm (physical + end correction)
    
    Returns:
        Resonance frequency in Hz
    """
    V = volume_litres / 1000.0  # m³
    r = (port_diameter_mm / 1000.0) / 2.0  # m
    S = np.pi * r**2  # m²
    L_eff = port_length_mm / 1000.0  # m
    
    # End correction: add 0.85 * diameter to each open end
    L_eff += 0.85 * (port_diameter_mm / 1000.0)
    
    f_b = (SPEED_OF_SOUND / (2 * np.pi)) * np.sqrt(S / (V * L_eff))
    return f_b


def port_air_velocity(port_diameter_mm: float, power_watts: float, 
                       sensitivity_db: float = 88.0, frequency_hz: float = 50.0) -> float:
    """
    Estimate peak air velocity through the port at a given power and frequency.
    
    High velocities (>15 m/s) cause audible chuffing noise.
    
    Args:
        port_diameter_mm: Inner diameter of the port in mm
        power_watts: Input power in watts
        sensitivity_db: Speaker sensitivity in dB SPL @ 1W/1m
        frequency_hz: Frequency of interest in Hz
    
    Returns:
        Approximate peak air velocity in m/s
    """
    r = (port_diameter_mm / 1000.0) / 2.0
    S = np.pi * r**2
    
    # Simplified estimate
    spl = sensitivity_db + 10 * np.log10(power_watts)
    p_rms = 2e-5 * 10**(spl / 20)
    
    # Volume velocity estimate
    v_peak = p_rms / (AIR_DENSITY * SPEED_OF_SOUND * S) * 10  # rough scaling
    return v_peak


class PortedEnclosure:
    """
    Ported (bass-reflex) enclosure model using Thiele-Small parameters.
    """
    
    def __init__(self, 
                 fs: float,          # Driver free-air resonance (Hz)
                 qts: float,         # Total Q factor
                 vas: float,         # Equivalent compliance volume (litres)
                 sd: float = None,   # Effective radiating area (cm²)
                 xmax: float = None, # Max linear excursion (mm)
                 re: float = 8.0,    # DC resistance (ohms)
                 sensitivity: float = 88.0  # dB SPL @ 1W/1m
                 ):
        self.fs = fs
        self.qts = qts
        self.vas = vas
        self.sd = sd
        self.xmax = xmax
        self.re = re
        self.sensitivity = sensitivity
    
    def optimal_volume(self) -> float:
        """Estimate optimal enclosure volume for a ported design (litres)."""
        # Rule of thumb: Vb ≈ 15 * Qts^2.87 * Vas
        vb = 15 * self.qts**2.87 * self.vas
        return vb
    
    def optimal_tuning(self, volume_litres: float = None) -> float:
        """Estimate optimal port tuning frequency (Hz)."""
        if volume_litres is None:
            volume_litres = self.optimal_volume()
        
        alpha = self.vas / volume_litres
        fb = (self.fs * alpha**0.44) / self.qts**0.205
        return fb
    
    def port_dimensions(self, volume_litres: float, target_fb: float, 
                        port_diameter_mm: float = 50.0) -> dict:
        """
        Calculate required port length for a given tuning frequency.
        
        Args:
            volume_litres: Enclosure internal volume in litres
            target_fb: Target tuning frequency in Hz
            port_diameter_mm: Desired port inner diameter in mm
            
        Returns:
            dict with port length, effective length, and air velocity estimate
        """
        V = volume_litres / 1000.0  # m³
        r = (port_diameter_mm / 1000.0) / 2.0
        S = np.pi * r**2
        
        # Rearrange Helmholtz: L_eff = S / (V * (2πfb/c)²)
        L_eff = S / (V * (2 * np.pi * target_fb / SPEED_OF_SOUND)**2)
        
        # Subtract end correction to get physical length
        end_correction = 0.85 * (port_diameter_mm / 1000.0)
        L_physical = L_eff - end_correction
        
        if L_physical < 0:
            L_physical = 0
        
        return {
            "port_diameter_mm": port_diameter_mm,
            "port_length_physical_mm": round(L_physical * 1000, 1),
            "port_length_effective_mm": round(L_eff * 1000, 1),
            "target_fb_hz": target_fb,
            "actual_fb_hz": round(port_resonance(volume_litres, port_diameter_mm, L_physical * 1000), 1),
        }
    
    def frequency_response(self, volume_litres: float, fb: float,
                           f_min: float = 20, f_max: float = 500, n_points: int = 500) -> tuple:
        """
        Calculate the normalised frequency response of the ported system.
        
        Returns:
            (frequencies, spl_db) numpy arrays
        """
        freqs = np.logspace(np.log10(f_min), np.log10(f_max), n_points)
        
        alpha = self.vas / volume_litres
        h = fb / self.fs
        
        spl = np.zeros_like(freqs)
        for i, f in enumerate(freqs):
            fn = f / self.fs  # normalised frequency
            
            # 4th-order high-pass transfer function for ported box
            s = 1j * fn
            num = s**4
            den = (s**4 + 
                   s**3 * (1 / self.qts) * (1 + alpha) / h +
                   s**2 * ((1 + alpha) + h**2 + alpha / (self.qts * h)) +
                   s * h / self.qts +
                   h**2)
            
            H = num / den
            spl[i] = 20 * np.log10(np.abs(H) + 1e-20)
        
        return freqs, spl
    
    def plot_response(self, volume_litres: float, fb: float, 
                      output_path: str = None, title: str = None) -> str:
        """
        Plot the frequency response and save to file.
        
        Returns:
            Path to saved plot image
        """
        freqs, spl = self.frequency_response(volume_litres, fb)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.semilogx(freqs, spl, 'b-', linewidth=2)
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Relative SPL (dB)')
        ax.set_title(title or f'Ported Enclosure Response — Vb={volume_litres:.1f}L, fb={fb:.0f}Hz')
        ax.set_xlim(20, 500)
        ax.set_ylim(-30, 6)
        ax.grid(True, which='both', alpha=0.3)
        ax.axhline(y=-3, color='r', linestyle='--', alpha=0.5, label='-3dB')
        ax.axhline(y=-6, color='orange', linestyle='--', alpha=0.5, label='-6dB')
        ax.legend()
        
        if output_path is None:
            output_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'acoustic_response.png'
            )
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=150)
        plt.close()
        return output_path
    
    def summary(self, volume_litres: float = None) -> str:
        """Print a summary of the enclosure design."""
        if volume_litres is None:
            volume_litres = self.optimal_volume()
        
        fb = self.optimal_tuning(volume_litres)
        
        lines = [
            "═" * 50,
            "  PORTED ENCLOSURE DESIGN SUMMARY",
            "═" * 50,
            f"  Driver Fs:        {self.fs:.1f} Hz",
            f"  Driver Qts:       {self.qts:.3f}",
            f"  Driver Vas:       {self.vas:.1f} L",
            f"  Sensitivity:      {self.sensitivity:.1f} dB",
            f"  Impedance:        {self.re:.1f} Ω",
            "─" * 50,
            f"  Enclosure Volume: {volume_litres:.1f} L",
            f"  Tuning Freq (fb): {fb:.1f} Hz",
            "─" * 50,
        ]
        
        # Calculate port for a few diameters
        for dia in [30, 40, 50, 60, 75]:
            pd = self.port_dimensions(volume_litres, fb, dia)
            lines.append(f"  Port Ø{dia}mm → length = {pd['port_length_physical_mm']:.0f} mm")
        
        lines.append("═" * 50)
        return "\n".join(lines)


# ─── Quick-access functions ───

def quick_design(fs, qts, vas, volume_litres=None):
    """Quick ported enclosure design from Thiele-Small parameters."""
    enc = PortedEnclosure(fs=fs, qts=qts, vas=vas)
    print(enc.summary(volume_litres))
    return enc


if __name__ == "__main__":
    # Demo with typical 5.25" woofer parameters
    # (These are placeholder values — replace with DS 100F measured T/S params)
    print("Demo: Typical 5.25\" woofer in ported enclosure\n")
    enc = PortedEnclosure(
        fs=55,       # Hz
        qts=0.38,    # typical for pro woofer
        vas=15.0,    # litres
        sensitivity=88.0,
    )
    print(enc.summary())
    
    # Port resonance calculator
    print(f"\nPort resonance (8L box, Ø40mm, 80mm long): "
          f"{port_resonance(8.0, 40.0, 80.0):.1f} Hz")
