from PIL import Image

def genData(data):

		newd = []

		for i in data:
			newd.append(format(ord(i), '08b'))
		return newd

# "{}".format()
def main():
	a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n"))
	if (a == 1):
		encode()

	elif (a == 2):
		print("Decoded Word : " + decode())
	else:
		raise Exception("Enter correct input")
	    
def modPix(pix, data):

	datalist = genData(data)
	lendata = len(datalist)
	imdata = iter(pix)

	for i in range(lendata):

		
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]]

		
		for j in range(0, 8):
			if (datalist[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
					pix[j] -= 1
				else:
					pix[j] += 1
				# pix[j] -= 1

		
		if (i == lendata - 1):
			if (pix[-1] % 2 == 0):
				if(pix[-1] != 0):
					pix[-1] -= 1
				else:
					pix[-1] += 1

		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1

		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]

def encode_enc(newimg, data):
	w = newimg.size[0]
	(x, y) = (0, 0)

	for pixel in modPix(newimg.getdata(), data):

		# Putting modified pixels in the new image
		newimg.putpixel((x, y), pixel)
		if (x == w - 1):
			x = 0
			y += 1
		else:
			x += 1

def encode():
	img = input("Enter image name (with extension): ")
	image = Image.open(img,'r')
	data = input("Please enter the data to be encoded: ")
	if len(data) == 0:
		raise ValueError("Data is empty")
	newimg = image.copy()
	encode_enc(newimg, data)
	newimg_name = input("Enter the name of the new image (with extension): ")
	newimg.save(newimg_name,str(newimg_name.split(".")[1].upper()))
	main()


def decode():
	img = input("Enter image name (with extension): ")
	image = Image.open(img,'r')
	data = ""
	imgData = iter(image.getdata())
	while True:
		pixel = [i for i in imgData.__next__()[:3]+imgData.__next__()[:3]+imgData.__next__()[:3]]
		#str of binary data
		binstr = ""
		for p in pixel[:8]:
			if p%2 == 0:
				binstr += "0"
			else:
				binstr += "1"
		data += chr(int(binstr,2)) #binary conversion, hence the base '2' (https://byjus.com/maths/binary-number-system/ )
		if pixel[-1] %2 !=0: #this condition checks if the the LSB of the last pixel is odd or not
			return data 

# Main Function


# Driver Code
if __name__ == '__main__' :

	# Calling main function
	main()
