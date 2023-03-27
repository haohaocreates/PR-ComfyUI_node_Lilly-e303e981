import os, glob, sys
import random
import re
import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] or __name__ =='__main__':
    from ConsoleColor import print, console
    from wildcards import wildcards
else:
    from .ConsoleColor import print, console
    from .wildcards import wildcards
#print(__file__)
#print(os.path.basename(__file__))

#print("wildcards_ComfyUI")
#print(os.getcwd())
#Wprint(f"CLIPTextEncodeWildcards __name__ {__name__}")

class CLIPTextEncodeWildcards:
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "text": ("STRING", {"multiline": True}), "clip": ("CLIP", )
        }
        }
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "conditioning"

    def encode(self, clip, text):
        print(f"[green]text : [/green]",text)
        r=wildcards.run(text)
        print(f"[green]encode : [/green]",r)
        return ([[clip.encode(r), {}]], )

class CLIPTextEncodeWildcards2:
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "text": ("STRING", {"multiline": True}), "clip": ("CLIP", ),
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            
        }
        }
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "conditioning"

    def encode(self, seed, clip, text):
        random.seed(seed)
        print(f"[green]text : [/green]",text)
        r=wildcards.run(text)
        print(f"[green]encode : [/green]",r)
        return ([[clip.encode(r), {}]], )
