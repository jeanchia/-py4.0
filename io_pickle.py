import pickle

# The name of the file where we will store the object
# 我们将储存的对象的文件名
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple','mango','carrot']


# Write to the file
f = open(shoplistfile,'wb')
# Dump the object to a file
pickle.dump(shoplist,f)
f.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile,'rb')
# load the object from the file
storedlist = pickle.load(f)
print(storedlist)

# 要想将一个对象存储到一个文件中，我们首先需要通过 open 以
# 写入（write）二进制（binary）模式打开文件，然后调用 pickle 模块的 dump 函数。
# 这一过程被称作封装（Pickling）。接着，我们通过 pickle 模块的 load 函数接收
# 返回的对象。这个过程被称作拆封（Unpickling）