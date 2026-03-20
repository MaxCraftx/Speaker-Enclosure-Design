import asyncio
import os
from zoo_mcp.ai_tools import text_to_cad

async def main():
    print("Sending prompt to Zoo Text-to-CAD engine...")
    print("This may take 10-30 seconds...")
    
    prompt = "A simple rectangular speaker enclosure box, 150mm high, 100mm wide, and 100mm deep, with a 75mm circular cutout in the center of the front face."
    
    try:
        # Call the text_to_cad tool directly
        result = await text_to_cad(prompt=prompt)
        
        output_file = "speaker_box_test.kcl"
        
        # Determine how to extract the string if result isn't a plain string
        if isinstance(result, str):
            code = result
        elif hasattr(result, "content"):
            code = result.content
        elif isinstance(result, list) and len(result) > 0 and hasattr(result[0], "text"):
            code = result[0].text
        else:
            code = str(result)
            
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(code)
        
        print(f"\n✅ Success! Model generated and saved to: {os.path.abspath(output_file)}")
        print("Open this file in Zoo Design Studio to view the 3D model.")
        
    except Exception as e:
        print(f"\n❌ Error generating model: {e}")

if __name__ == "__main__":
    asyncio.run(main())
