import os
from sklearn import cluster
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import sklearn.metrics as metrics
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, set_link_color_palette
import time

file1 = os.listdir('C:/Users/abc86/Desktop/mini_newsgroups')
#print('資料夾下的內容\n',file1)


train = []
y=[]

for name in file1:
    path = 'C:/Users/abc86/Desktop/mini_newsgroups/'+ name
    files= os.listdir(path) 
    for file in files: 
         if not os.path.isdir(file): 
              f = open(path+"/"+file,encoding='cp1252'); 
              iter_f = iter(f); 
              str = ""
              for line in iter_f: 
                  str = str + line
              y.append(name)
              train.append(str)
    #print(train) 
    #print(y)


vectorizer = CountVectorizer()
a=vectorizer.fit_transform(train)
#print(a)
abcdf=TfidfTransformer()
b=abcdf.fit_transform(a)
#print(b)

start = time.time()
hclust = cluster.AgglomerativeClustering(linkage = 'ward', affinity = 'euclidean', n_clusters = 20)
hclust.fit(b.toarray())  #b 需要轉型成陣列
cluster_labels = hclust.labels_
silhouette_avg = metrics.silhouette_score(b.toarray(), cluster_labels)  #b 需要轉型成陣列
end = time.time()
print(silhouette_avg)
print("time : %f" %(end-start))



from scipy.cluster import hierarchy

Z = hierarchy.linkage(b.toarray(), method ='ward',metric='euclidean')
dendrogram(Z, truncate_mode='level', p=3)
plt.show()




