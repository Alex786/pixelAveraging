'''
pixelAveraging.py
Alexander Brown
HW 16 Pixel Averaging
11-15-23
'''

def readPpmFile(PpmFilePath):
    with open(PpmFilePath, 'r') as file:
        
        '''Read header'''
        P3Info = file.readline().strip()
        width, height = map(int, file.readline().split())
        maxColor255 = int(file.readline().strip())

        '''Read pixel data'''
        pixels = []
        for pixelAverageCalculation in range(width * height):
            pixel = list(map(int, file.readline().split()))
            pixels.append(pixel)

    file.close()
    return P3Info, width, height, maxColor255, pixels

def averageImageSet(selectedImageSet):
    numOfImages = 10
    totalPixels = []

    '''Read and get pixel values from all images in the set'''
    for i in range(1, numOfImages + 1):
        PpmFilePath = f"{selectedImageSet}/{selectedImageSet}_{i}.ppm"
        _, width, height, _, pixels = readPpmFile(PpmFilePath)

        if i == 1:
            totalPixels = pixels
        else:
            for j in range(len(totalPixels)):
                
                '''Red, Green, Blue components'''
                for k in range(3):  
                    totalPixels[j][k] += pixels[j][k]

    '''Calculate average pixel values'''
    for i in range(len(totalPixels)):
        for j in range(3):
            totalPixels[i][j] //= numOfImages

    '''Write averaged image to a new file'''
    NewGoodPpmFilePath = f"{selectedImageSet}/{selectedImageSet}.ppm"
    writePpmFile(NewGoodPpmFilePath, "P3", width, height, 255, totalPixels)

def writePpmFile(PpmFilePath, P3Info, width, height, maxColor255, pixels):
    with open(PpmFilePath, 'w') as file:
        
        '''Write header'''
        file.write(f"{P3Info}\n")
        file.write(f"{width} {height}\n")
        file.write(f"{maxColor255}\n")

        '''Write pixel data'''
        for pixel in pixels:
            file.write(" ".join(map(str, pixel)) + "\n")

    file.close()

def main():
    imageSets = {
        '1': 'cone_nebula',
        '2': 'n44f',
        '3': 'orion',
        '4': 'wfc3_uvis'
    }

    print("Which image set do you want to process?")
    print(" 1) cone_nebula (The Cone Nebula - NGC 2264)")
    print(" 2) n44f (Interstellar Bubble N44F)")
    print(" 3) orion (The Orion Nebula)")
    print(" 4) wfc3_uvis (Carina Nebula)")

    choice = input("Selection: ")

    if choice in imageSets:
        selectedImageSet = imageSets[choice]
        averageImageSet(selectedImageSet)
        print(f"good image saved to {selectedImageSet}/{selectedImageSet}.ppm")
    else:
        print("Enter 1 through 4.")

main()