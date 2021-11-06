"""
    Class that handles loading/saving of RAW/other formats.
    If images are of a regular filetype (jpg, png, ...); they are opened using opencv.
    Else use rawpy to load RAW image.
"""
import rawpy

# All RAW formats; src: https://fileinfo.com/filetypes/camera_raw
supported_raw_formats = [
    "RWZ",
    "RW2",
    "CR2",
    "DNG",
    "ERF",
    "NRW",
    "RAF",
    "ARW",
    "NEF",
    "K25",
    "DNG",
    "SRF",
    "EIP",
    "DCR",
    "RAW",
    "CRW",
    "3FR",
    "BAY",
    "MEF",
    "CS1",
    "KDC",
    "ORF",
    "ARI",
    "SR2",
    "MOS",
    "MFW",
    "CR3",
    "FFF",
    "SRW",
    "J6I",
    "X3F",
    "KC2",
    "RWL",
    "MRW",
    "PEF",
    "IIQ",
    "CXI",
    "MDC",
]
# Open-cv imread supported formats; src: https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
supported_regular_formats = [
    "bmp",
    "dib",
    "jpeg",
    "jpg",
    "jpe",
    "jp2",
    "png",
    "webp",
    "pbm",
    "pgm",
    "ppm",
    "pxm",
    "pnm",
    "pfm",
    "sr",
    "ras",
    "tiff",
    "tif",
    "exr",
    "hdr",
    "pic",
]
