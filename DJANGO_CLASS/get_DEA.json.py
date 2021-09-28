import sys
import geocoder

result = geocoder(sys.argv[1:])
print(result[0].coordinates)