---
title: Plotly
description: "The Figurl Plotly interface allows any Plotly figure created in Python to be shared as a Figurl figure."
category: general
image: "https://user-images.githubusercontent.com/3679296/214572992-bc9a7c8a-69d3-4885-8797-045260cdbefc.png"
---

# Plotly

[Plotly](https://plotly.com/graphing-libraries/) is a data visualization library for Python and other languages. It is used to create interactive and dynamic graphs and charts, including line charts, bar charts, scatter plots, histograms, pie charts, and more. It also provides tools for creating maps, 3D graphs, and other visualizations.

The Figurl Plotly interface allows any Plotly figure created in Python to be shared as a Figurl figure. Here is an example script for creating a 3D rotatable scatter plot.

<!--------------------------------------------------------------------------------------------->
<figure>
<a name="figure-plotly-script"></a>

```python
import plotly.express as px
import figurl as fig

# Example from: https://plotly.com/python/3d-scatter-plots/
iris = px.data.iris()
ff = px.scatter_3d(
    iris,
    x='sepal_length', y='sepal_width', z='petal_width',
    color='species'
)

# Create and print the figURL
url = fig.Plotly(ff).url(label='plotly example - iris 3d')
print(url)

# Output: 
# https://figurl.org/f?v=gs://figurl/plotly-1&d=sha1://5c6ec276ce9a3b20b208aaff911b037ce4052e51&label=plotly%20example%20-%20iris%203d
```

<figcaption>

Figure 1. Example script demonstrating the Figurl Plotly integration.

</figcaption>
</figure>
<!--------------------------------------------------------------------------------------------->

And here is the resulting figure.

<!--------------------------------------------------------------------------------------------->
<figure>
<a name="figure-plotly"></a>

https://figurl.org/f?v=gs://figurl/plotly-1&d=sha1://5c6ec276ce9a3b20b208aaff911b037ce4052e51&label=plotly%20example%20-%20iris%203d
<!--
height: 500
-->
<figcaption>

Figure 2. Interactive Plotly Figurl figure

</figcaption>
</figure>
<!--------------------------------------------------------------------------------------------->

For more examples of Plotly graphs, see [this gallery](https://plotly.com/python/basic-charts).