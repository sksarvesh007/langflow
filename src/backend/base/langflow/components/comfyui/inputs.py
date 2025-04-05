from langflow.base.data import BaseFileComponent
from langflow.base.data.utils import TEXT_FILE_TYPES, parallel_load_data, parse_text_file_to_data
from langflow.io import BoolInput, IntInput, MessageInput, FileInput
from langflow.schema import Data

class ComfyUIComponent(BaseFileComponent):
    display_name = "ComfyUI"
    description = "ComfyUI is a web application for creating and sharing AI-generated images."
    icon = "ComfyUI"
    name = "ComfyUI"
    
    # Supported image extensions
    VALID_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.webp', '.bmp']

    inputs = [
        *BaseFileComponent._base_inputs,
        FileInput(
            name="image",
            display_name="Image Upload",
            info="Upload an image to process",
            file_types=VALID_EXTENSIONS
        ),
        MessageInput(
            name="prompt",
            display_name="Prompt",
            info="The prompt to use for the image",
        )
    ]
    
    outputs = [
        *BaseFileComponent._base_outputs,
    ]

    def process_files(self, file_list: list[BaseFileComponent.BaseFile]) -> list[BaseFileComponent.BaseFile]:
        """Simply return the uploaded files without processing"""
        return file_list
    
    
