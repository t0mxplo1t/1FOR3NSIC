import exif,os

from exif import Image
from os.path import exists

def banner():
	print("""\033[33m
 ██╗███████╗ ██████╗ ██████╗ ██████╗ ███╗   ██╗▄▄███▄▄·██╗ ██████╗
███║██╔════╝██╔═══██╗██╔══██╗╚════██╗████╗  ██║██╔════╝██║██╔════╝
╚██║█████╗  ██║   ██║██████╔╝ █████╔╝██╔██╗ ██║███████╗██║██║
 ██║██╔══╝  ██║   ██║██╔══██╗ ╚═══██╗██║╚██╗██║╚════██║██║██║
 ██║██║     ╚██████╔╝██║  ██║██████╔╝██║ ╚████║███████║██║╚██████╗
 ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═▀▀▀══╝╚═╝ ╚═════╝\033[0m
\033[41mExtract Information from a Photo | Image Forensic | Github T0mxplo1t\033[0m\n""")
banner()

def informasi():
	print("\033[0;33m+---------------------+")
	print("\033[0;33m|\033[0m \033[1;41m>>> Information <<<\033[0m \033[0;33m|")
	print("+---------------------+\033[0m")
	print("\033[1;36mHas EXIF >\033[0m",pic.has_exif)
	print("\033[1;36mDevice model >\033[0m",pic.model)
	print("\033[1;36mOrientation >\033[0m",pic.orientation)
	print("\033[1;36mDate & time >\033[0m",pic.datetime)
	print("\033[1;36mEXIF IFD pointer >\033[0m",pic._exif_ifd_pointer)
	print("\033[1;36mGPS IFD pointer >\033[0m",pic._gps_ifd_pointer)
	print("\033[1;36mDevice name >\033[0m",pic.make)
	print("\033[1;36mF number >\033[0m",pic.f_number)
	print("\033[1;36mExposure time >\033[0m",pic.exposure_time)
	print("\033[1;36mFocal length >\033[0m",pic.focal_length)
	print("\033[1;36mFlash >\033[0m",pic.flash)
	print("\033[1;36mMetering mode >\033[0m",pic.metering_mode)
	print("\033[1;36mPhotographiv sensitivity >\033[0m",pic.photographic_sensitivity)
	print("\033[1;36mFocal length in 35mm film >\033[0m",pic.focal_length_in_35mm_film)
	print("\033[1;36mMax aperture value >\033[0m",pic.max_aperture_value)
	print("\033[1;36mDatetime digitized >\033[0m",pic.datetime_digitized)
	print("\033[1;36mExposure bias value >\033[0m",pic.exposure_bias_value)
	print("\033[1;36mWhite balance >\033[0m",pic.white_balance)
	print("\033[1;36mOriginal date & time >\033[0m",pic.datetime_original)
	print("\033[1;36mAperture value >\033[0m",pic.aperture_value)
	print("\033[1;36mGPS latitude ref >\033[0m",pic.gps_latitude_ref)
	print("\033[1;36mGPS latitude >\033[0m",pic.gps_latitude)
	print("\033[1;36mGPS longitude ref >\033[0m",pic.gps_longitude_ref)
	print("\033[1;36mGPS longitude >\033[0m",pic.gps_longitude)

try:
	file = input("\033[1;32mEnter the file location\033[0m [\033[30;42m/data/files/pictures/image.jpg\033[0m]\n")
	# Memeriksa apakah file ada di sistem
	if exists(file):
		print("\033[1;32m>>> File exists!\033[0m")
		with open(file, "rb") as img:
			pic = Image(img)
			informasi()
	else:
		print("\033[1;32m>>> File does not exist!\033[0m")

except EOFError:
	print("\033[1;32mCrott ah..\033[0m")

except KeyboardInterrupt:
	print("\033[1;32mOkay\033[0m")
