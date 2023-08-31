import React from 'react'

import '../styles/styles.css'
// import Day from './Day'
const CityInfo = ({ info, finishedQuery }) => {
  console.log("INFO!", info)
  return (
    <div className="container">
      {(finishedQuery && info !== undefined && info.hasOwnProperty("total_time")) ? (
        <div>
          <h1> Time in location: {info.total_time}</h1>
          {Object.entries(info.days).map((itm, indx) => {
            console.log(itm[1].morning_activities)
            return (
              <article key={indx} className="episode">
                <div className="episode__number">0{indx+1}</div>
                <div className="episode__content">
                  <div className="title"> Day 0{indx+1}</div>
                    <div className="story">
                    <h5>Morning: </h5>
                    {itm[1].morning_activities.map((morning_activity, m_indx) => {
                      return (
                        <div key={m_indx}>
                          <span>{morning_activity}</span>
                        </div>
                      )
                    })}
                    <h5>Afternoon: </h5>
                    {itm[1].afternoon_activities.map((afternoon_activity, m_indx) => {
                      return (
                        <div key={m_indx}>
                          <span>{afternoon_activity}</span>
                        </div>
                      )
                    })}
                    <h5>Evening: </h5>
                    {itm[1].evening_activities.map((evening_activity, m_indx) => {
                      return (
                        <div key={m_indx}>
                          <span>{evening_activity}</span>
                        </div>
                      )
                    })}
                  </div>
                </div>
              </article>
            )
          })}
        </div>
      ) : (<div></div>)}
    </div>
  )
}
export default CityInfo
