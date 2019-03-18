import pickle as p

shoplistfile = 'shoplist.data'
shoplist = ['apple','mongo','carrot']
f = file(shoplistfile,'wb')
p.dump(shoplist,f)
f.close()

f = file(shoplistfile)
storedlist = p.load(f)
print(storedlist)