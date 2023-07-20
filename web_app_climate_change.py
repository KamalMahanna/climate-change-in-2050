import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go

st.title("How I see my life in 2050, in a world that may not have tackled effects of climate change very well")
st.write("In the year 2050, several changes might happen to the climate, including global warming, decreasing oxygen level(air pollution), pure water shortage, Soil sortage. Let's discuss them briefly below.")
# st.header('Global Oxyzen(O₂) level')

components.html ('<h3>Global Oxyzen(O₂) level:</h3>')

components.html("""
                <div id="o2-widget-container"></div><script type="text/javascript" src="https://www.climatelevels.org/graphs/js/o2.php?theme=default&pid=2degreesinstitute"></script>
                """,
                height=395)
st.text("")

st.write("Here ppm means parts per meg i.e. one molecule of Oxygen over one million of Oxygen. From the above graph it is clear oxygen level is decreasing drastically over the years. In the future, Oxygen shortage might cause the extinction of living creatures. 50% increase in carbon emission due to human action, but also notice this is the data from 2016. Let's have a look at the CO₂ level over the past years.")

# st.header('Global Oxyzen(O₂) level')
components.html('<h3>Global Carbon Dioxide(CO₂) level:</h3>')



st.image("https://www.visualcapitalist.com/wp-content/uploads/2020/11/GHG-Emissions-By-Sector-1200px.png")
st.text("")
st.write("50% increase in carbon emission due to human action, but also notice this is the data from 2016. Lets have a look at the CO₂ level over past years.")

components.html("""
                <div id="co2-widget-container"></div><script type="text/javascript" src="https://www.climatelevels.org/graphs/js/co2.php?theme=default&pid=2degreesinstitute"></script>
                """,height=395)
st.text("")

st.write("After the year 1850, the CO₂ level increased exponentially. Result will increase the temperature of the atmosphere. Life will struggle to intake fresh air because of less oxygen in the air. The public will be using masks every time. We might have to purchase oxygen cylinders because of less oxygen in the air.")

st.text("")
components.html ('<h3>Rising in temperature:</h3>')

components.html("""
                <div id="temperature-widget-container"></div><script type="text/javascript" src="https://www.climatelevels.org/graphs/js/temperature.php?theme=default&pid=2degreesinstitute"></script>
                """,height=395)
st.text("")

st.write("On an average .28°C is increasing every year. High temperature can lead to extremely bad weather conditions, glaciers may melt which will increase the sea level, and some species like cold-weathered animals might extinct from the earth. Every dry-tropical forest (less rainy forest) might catch fire.")
st.text("")
st.text("")

components.html("""
                <div id="sealevels-widget-container"></div><script type="text/javascript" src="https://www.climatelevels.org/graphs/js/sealevels.php?theme=default&pid=2degreesinstitute"></script>
                """,height=395)
st.text("")

st.write("There will be a direct relation between the rise in seawater level with temperature. High temperature will cause melting snow, results increase in seawater level.")



st.text("")

st.header('So, Will Life End On Earth?')

st.write('So, the answer lies in the past, when life was created, many evolutions took place, and life found a way to survive. 30 years from now, all those disasters might not happen, but some of them will. We might prepare an underground tunnel to stay protected from high temperatures. Elon Musk may become successful in sending people to Mars, so we will be settled on Mars. Or people all over the world decided to reduce carbon emissions and plant trees so that the climate becomes normal. At last, there might be some genetic changes that appear to adapt to the environment.')
