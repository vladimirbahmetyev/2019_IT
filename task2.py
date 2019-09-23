from math import exp
import matplotlib.pyplot as plt
import numpy as np


def gaussian(x, mu, sigma): return exp(-(((x - mu) / sigma) ** 2) / 2.0)


def gaussKernel(kernelRadius, sigma):
    hKernel = [gaussian(x, kernelRadius, sigma) for x in range(2 * kernelRadius + 1)]
    vKernel = [x for x in hKernel]
    kernel = [[xh * xv for xh in hKernel] for xv in vKernel]
    kernelSum = sum([sum(row) for row in kernel])
    kernel = [[x / kernelSum for x in row] for row in kernel]
    return np.array([np.array(xi) for xi in kernel])


def filterGauss(img, matrixSize):
    imgGauss = np.zeros_like(img)
    kernel = gaussKernel(matrixSize // 2, 10)
    padding = matrixSize // 2
    for i in range(matrixSize // 2, img.shape[0] - matrixSize // 2):
        for j in range(matrixSize // 2, img.shape[1] - matrixSize // 2):
            for c in range(img.shape[2]):
                conv = img[i - padding:i + padding + 1, j - padding:j + padding + 1, c] * kernel
                imgGauss[i, j, c] = conv.sum()

    return imgGauss


def main():
    img = plt.imread("go.png")[:, :, :3]
    img2 = filterGauss(img, 22)

    fig, axs = plt.subplots(1, 2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()
