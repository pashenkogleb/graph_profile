import IPython
from IPython.core.magic import register_cell_magic



@register_cell_magic
def graph_profile(line, cell):
    ipython = IPython.get_ipython()
    ipython.run_cell_magic("prun", "-D /tmp/temprorary_profile.profile", cell)
    ipython.system("gprof2dot -f pstats /tmp/temprorary_profile.profile  > /tmp/temprorary_profile.dot")
    ipython.system("dot -Tjpg /tmp/temprorary_profile.dot -o profile_res.jpg")
    print("output in profile_res.jpg")