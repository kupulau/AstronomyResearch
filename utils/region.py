# This is the code for making ds9 region files

# refs
# https://ds9.si.edu/doc/ref/region.html
# https://www.stsci.edu/scientific-community/software/drizzlepac/examples/using-ds9-regions
# https://astropy-regions.readthedocs.io/en/stable/region_io.html
# https://fermi.gsfc.nasa.gov/ssc/data/access/lat/fava_catalog/2FAV_v10_sources.reg

# one point in a region file
def ds9region(name, ra, dec, color, text=None, size=20):
    '''
    name = ds9 region name [str]
    ra = ra in deg [float]
    dec = dec in deg [float]
    color = region color [str]
    size = radius of region in arcsec [float]
    '''
    txt = """# Region file format: DS9 version 4.1\nglobal color={} dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\ncircle({},{},{}") # text={}""".format(color, ra, dec, size, text)
    f = open('{}.reg'.format(name), 'w')
    f.write(txt)
    f.close()

# example
ds9region('NGC6946', 308.718, 60.153, 'green', text='galaxy', size=10)



# multiple points in a region file
def ds9regions(name, ra, dec, color, text=None, size=20):   
    '''
    name = ds9 region name [str]
    ra = ra list in deg [float]
    dec = dec list in deg [float]
    color = color of region [str]
    text = text list [str]
    size = radius list in arcsec [float]
    '''
    txt1 =  """# Region file format: DS9 version 4.1\nglobal color={} dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5""".format(color)

    tlist = []
    for i in range(len(ra)):
        t = '\ncircle({},{},{}") # text={}'.format(ra[i], dec[i], size[i], text[i])
        tlist.append(t)    
    txt2 = ' '.join(tlist)
    
    txt = txt1 + txt2
    
    f = open('{}.reg'.format(name), 'w')
    f.write(txt)
    f.close()    
    
# example    
ds9regions('stars', tbl['RA'], tbl['Dec'], color='red', text=textlist, size=sizelist)