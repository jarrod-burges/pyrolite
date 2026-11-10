import matplotlib

from ...util.plot.axes import init_axes
from ...util.classification import AIOCG
from ...util.meta import sphinx_doi_link, update_docstring_references, subkwargs
from ...util.log import Handle

logger = Handle(__name__)


@update_docstring_references
def AIOCG(
    ax: matplotlib.axes.Axes | None = None,
    add_labels: bool = False,
    relim: bool = True,
    color: str = "k",
    **kwargs,
) -> matplotlib.axes.Axes:
    """
     IOCG alteration discrimination diagram for main IOCG alteration types (Na, Ca-Fe, K-Fe and K)
     from Montreuil et al. (2013) [#ref_1]_ to an axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to add the diagram to.
    add_labels : bool
        Whether to add labels at polygon centroids.
    relim : bool
        Whether to relimit axes to the default range for this diagram.
    color : str
        Color for the polygon edges in the diagram.

    References
    -----------
    .. [#ref_1] Montreuil J F, Corriveau L, and Potter E G (2015). Formation of 
            albitite-hosted uranium within IOCG systems: the Southern Breccia, 
            Great Bear magmatic zone, Northwest Territories, Canada. 
            Mineralium Deposita, 50:293-325.
            doi:{Montreuil2013}
    """
    ax = init_axes(ax=ax, **kwargs)

    clf = AIOCG()

    ax = clf.add_to_axes(
        ax=ax, color=color, add_labels=add_labels, **kwargs
    )

    if relim:
        ax.set(xlim=clf.lims["xlim"], ylim=clf.lims["ylim"])
    return ax


AIOCG.__doc__ = AIOCG.__doc__.format(
    Montreuil2013=sphinx_doi_link("10.1007/s00126-014-0530-7")
)
