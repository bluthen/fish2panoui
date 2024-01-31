import cv2
import fish2pano

def main():
    if len(sys.argv) < 6:
        print("Usage: %s [image] [radius] [centerx,centery] [scale_factor] [outfile_name]" % (sys.argv[0],))
        sys.exit(1)
    imgfile = sys.argv[1]
    radius = float(sys.argv[2])
    center = [float(x) for x in sys.argv[3].split(',')]
    scale = float(sys.argv[4])
    outfile = sys.argv[5]
    img_raw = cv2.imread(imgfile)
    img_t = fish2pano.fish2pano(img_raw, radius, center, scale)
    cv2.imshow('transformed', img_t)
    cv2.waitKey()
    cv2.imwrite(outfile, img_t)


if __name__ == '__main__':
    main()
