---
title: Altair
description: "The Figurl Altair interface allows any Altair chart created in Python to be shared as a Figurl figure."
category: general
image: "https://user-images.githubusercontent.com/3679296/214572794-23fea302-a727-47ff-bf8b-f81385045707.png"
---

# Altair

[Altair](https://altair-viz.github.io/) is a powerful declarative visualization library for Python that specializes in interactive statistical plots. It is based on Vega and Vega-Lite, 

The Figurl Altair interface allows any Altair chart created in Python to be shared as a Figurl figure. Here is an example script for creating an Altair chart.

<!--------------------------------------------------------------------------------------------->
<figure>
<a name="figure-altair-script"></a>

```python
import figurl as fig

# This example is from: https://altair-viz.github.io/gallery/simple_histogram.html
import altair as alt
from vega_datasets import data

source = data.movies.url

chart = alt.Chart(source).mark_bar().encode(
    alt.X("IMDB_Rating:Q", bin=True),
    y='count()',
)

# Create and print the figURL
url = fig.Altair(chart).url(label='example altair chart')
print(url)

# Output: 
# https://figurl.org/f?v=gs://figurl/vegalite-2&d=sha1://f5920cbea57e42211f7cf83065230132713a3f01&label=example%20altair%20chart
```

<figcaption>

Figure 1. Example script demonstrating the Figurl Altair integration.

</figcaption>
</figure>
<!--------------------------------------------------------------------------------------------->

And here is the resulting figure.

<!--------------------------------------------------------------------------------------------->
<figure>
<a name="figure-altair"></a>

https://figurl.org/f?v=gs://figurl/vegalite-2&d=sha1://f5920cbea57e42211f7cf83065230132713a3f01&label=example%20altair%20chart
<!--
height: 500
-->
<figcaption>

Figure 2. Interactive Altair Figurl figure

</figcaption>
</figure>
<!--------------------------------------------------------------------------------------------->

For more examples of Altair charts, see [this gallery](https://altair-viz.github.io/gallery/index.html).