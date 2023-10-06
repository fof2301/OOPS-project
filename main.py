import binascii
import text_to_image
#file to hex
filename = "provide the filename"
with open(filename, "rb") as f:
  content=f.read()
  hex_Data=binascii.hexlify(content)
with open("textfile.txt", 'wb') as f:
    f.write(hex_Data)
#encoded image generator
encoded_image_path = text_to_image.encode_file("textfile.txt", "output_image.png")    
#decoder 
decoded_file_path = text_to_image.decode_to_file("output_image.png","test.txt")
#hex to file
import binascii
with open("test.txt") as f, open("out", 'wb') as out:
    for line in f:
        out.write(binascii.unhexlify(''.join(line.split())))
