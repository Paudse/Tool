from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
import io

# fig setup
fig = plt.figure(figsize=(6,5), dpi=300)

x = np.arange(0, 50, 0.1)

y1 = 0.1**x
y3 = 0.3**x
y5 = 0.5**x
y7 = 0.7**x
y9 = 0.9**x
y95 = 0.95**x
y97 = 0.97**x
y99 = 0.99**x

##plt.rcParams['figure.figsize'] = (8.0, 4.0) # 设置figure_size尺寸
##plt.rcParams['savefig.dpi'] = 300 #图片像素
####plt.rcParams['figure.dpi'] = 300 #分辨率

plt.subplot(211)
plt.plot(x, y1, color="r", linestyle="-", linewidth=1)
##plt.plot(x, y3, color="darkorange", linestyle="-", linewidth=1)
plt.plot(x, y5, color="gold", linestyle="-", linewidth=1)
plt.plot(x, y7, color="lawngreen", linestyle="-", linewidth=1)
plt.plot(x, y9, color="g", linestyle="-", linewidth=1)
plt.plot(x, y95, color="royalblue", linestyle="-", linewidth=1)
plt.plot(x, y97, color="mediumblue", linestyle="-", linewidth=1)
plt.plot(x, y99, color="indigo", linestyle="-", linewidth=1)

plt.grid(True)

##plt.text(9, 0.1, "$\\mathregular{0.1^{x}}$", fontsize=10)
##plt.text(7, 0.2, "$\\mathregular{0.5^{x}}$", fontsize=10)
plt.text(3, 0.37, "$\\mathregular{0.7^{x}}$", fontsize=10)
plt.text(20, 0.13, "$\\mathregular{0.9^{x}}$", fontsize=10)
plt.text(25, 0.29, "$\\mathregular{0.95^{x}}$", fontsize=10)
plt.text(30, 0.41, "$\\mathregular{0.97^{x}}$", fontsize=10)
plt.text(35, 0.71, "$\\mathregular{0.99^{x}}$", fontsize=10)

plt.annotate('$\\mathregular{0.1^{x}}$', xy=(2, 0.1**2), xytext=(9, 0.1), arrowprops=dict(facecolor='k', headwidth=4, width=0.5))
plt.annotate('$\\mathregular{0.5^{x}}$', xy=(3, 0.5**3), xytext=(7, 0.2), arrowprops=dict(facecolor='k', headwidth=4, width=0.5))
##plt.annotate('$\\mathregular{0.7^{x}}$', xy=(4, 0.7**4), xytext=(5, 0.3), arrowprops=dict(facecolor='k', headwidth=4, width=0.5))
##plt.annotate('$\\mathregular{0.9^{x}}$', xy=(18, 0.9**18), xytext=(20, 0.16), arrowprops=dict(facecolor='k', headwidth=0.5, width=0.5))
##plt.annotate('$\\mathregular{0.95^{x}}$', xy=(23, 0.95**23), xytext=(25, 0.32), arrowprops=dict(facecolor='k', headwidth=0.5, width=0.5))
##plt.annotate('$\\mathregular{0.97^{x}}$', xy=(28, 0.97**28), xytext=(30, 0.45), arrowprops=dict(facecolor='k', headwidth=0.5, width=0.5))
##plt.annotate('$\\mathregular{0.99^{x}}$', xy=(33, 0.99**33), xytext=(35, 0.74), arrowprops=dict(facecolor='k', headwidth=0.5, width=0.5))

plt.xlabel("x")
plt.ylabel("y")

##plt.show()

#fig.savefig('3dPlot.pdf')

# Save the image in memory in PNG format
png1 = io.BytesIO()
fig.savefig(png1, format="png")

# Load this image into PIL
png2 = Image.open(png1)

# Save as TIFF
png2.save("save.tiff")
png1.close()
