#export PATH=~/anaconda/bin:$PATH;


from ete3 import Tree, faces, AttrFace, TreeStyle, NodeStyle


def remove_errors_in_trees(fin):
    """
    Import newick tree.
    Load each tree to check if there are any errors.
    Create new file for error-free trees, 
    and which tree have errors.
    """  
    f=open(fin,'r')
    trees=f.read().split('\n')
    f.close()
    error_tree_trees=[]
    for num,tree in enumerate(trees):
        try:
            t = Tree(tree)
        except:
            f=open(fin1.replace('.txt','_errors.txt'),'a')
            f.write('\t'.join([str(i),str(num)])+'\n')
            f.close()
        else:
            error_tree_trees.append(tree)
    f=open(fin1.replace('.txt','.error_free.txt'),'w')
    f.write('\n'.join(error_tree_trees))
    f.close()

for i in [1,2,3,4,5]:
    fin1='ribosome_concat_'+str(i)+'.phy_phyml_boot_trees.txt'
    remove_errors_in_trees(fin)




