
import React, {useState} from 'react';

import { AwesomeButton } from 'react-awesome-button';
import ReactLoading from "react-loading";
import 'react-awesome-button/dist/styles.css';
import './styles/styles.css'

import './App.css';
import  CityInfo from "./components/CityInfo"
import  Events from "./components/Events"

function App() {
  const [currentLocation, setCurrentLoc] = useState(0);
  const [gpt_data, setGPTData] = useState("")
  const [finishedQuery, setDone] = useState(true);
  const [currentEvents, setEvents] = useState({})

  /**
   *
   * @returns
   */
  const getCityAndState = async () => {
    const locationData = await fetch('/location')
    return locationData.json()
  }

  /**
   *
   * @returns
   */
  const getGPTText = async (city, state) => {
    const gptText = await fetch('/gpt-data/' + city + "/" + state)
    return gptText.json()
  }

  const getCurrentEvents = async (city, state) => {
    const event = await fetch("/google-events/" + city + "/" + state + "/")
    return event.json()
  }

  /**
   *
   */
  const handleClick = async () => {
      console.log("Handling click....")
      try {
        setDone(false)
        const locationData = await getCityAndState();
        setCurrentLoc(locationData);
        const curEvents = await getCurrentEvents(locationData.city, locationData.state);
        setEvents(curEvents.events);
        const gptText = await getGPTText(locationData.city, locationData.state);
        setGPTData(gptText.gpt_data);
        setDone(true)
      } catch (err) {
        console.log(err.message)
        setDone(true);
      }
  }

  return (

    <div className="App">
      <header className="App">
        <h1>CHOOSE YOUR OWN ADVENTURE</h1>
        <br></br>
        <AwesomeButton
          type="secondary"
          ripple={true}
          onPress={handleClick}
          size="large">
          Click Me To Discover
        </AwesomeButton>
      </header>

      <body>

        {!finishedQuery ? (
            <ReactLoading className="loading-bar" type={"bubbles"} color={"#FFFFFF"} height={100} width={100} />
          ) : (
            <div>
              <h3>{currentLocation === 0 ? "Time To Go!" : "Want To Explore " + currentLocation.location + "?" }</h3>
              <br></br>
              <CityInfo info={gpt_data} finishedQuery={finishedQuery}/>
              <Events currentEvents={currentEvents} queryState={finishedQuery}/>
            </div>
          )}
      </body>
    </div>
  );
}

export default App;
