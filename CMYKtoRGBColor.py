# Rumus untuk mengubah RGB ke CMYK
def rgb_to_cmy(r,b,g):

# Nilai RGB dibagi 255
# Untuk membawa mereka antara 0 hingga 1.
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    return (c,m,y)

# Contoh nilai RGB.
r = 0
g = 169
b = 86

#cetak hasil
print(rgb_to_cmy(r,g,b))