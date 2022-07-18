import IPython
from IPython.core.magic import register_cell_magic
import tempfile


@register_cell_magic
def graph_profile(line, cell):
    '''
    can provide file name in line 
    '''

    if line =='':
        jpg_file = tempfile.NamedTemporaryFile(suffix = ".jpg")
    else:
        jpg_file = open(line, "w")
    
    ipython = IPython.get_ipython()
    profile_file = tempfile.NamedTemporaryFile(suffix = ".profile")
    dot_file = tempfile.NamedTemporaryFile(suffix = ".dot")
    

    ipython.run_cell_magic("prun", f"-q -D {profile_file.name}", cell) #q to supress output
    ipython.system(f"gprof2dot -f pstats {profile_file.name}  > {dot_file.name}")
    ipython.system(f"dot -Tjpg {dot_file.name} -o {jpg_file.name}")
    

    IPython.display.Image(filename = jpg_file.name)

    res =  IPython.display.Image(filename = f"{jpg_file.name}", format= "jpg")
    for f in [profile_file,dot_file,jpg_file]:
        f.close()


    return res

    # ipython.run_cell_magic("prun", "-D /tmp/temprorary_profile.profile", cell)
    #ipython.system("gprof2dot -f pstats /tmp/temprorary_profile.profile  > /tmp/temprorary_profile.dot")

    #ipython.system("dot -Tjpg /tmp/temprorary_profile.dot -o profile_res.jpg")
    #print("output in profile_res.jpg")