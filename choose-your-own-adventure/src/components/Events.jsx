
const Events = ({ currentEvents, queryState}) => {
  return (
    <div className="relative flex items-center">
        <div id="slider" className="w-full h-full overflow-x-scroll scroll whitespace-nowrap">
        {(queryState && currentEvents !== undefined) ? (
          Object.entries(currentEvents).map((itm, indx) => {
            if (itm[1].status === "error"){
              return <h2> Unfortunately There Are No Upcoming Events!</h2>
            }
            return (
              <div key={indx} className="w-[220px] inline-block p-2 cursor-pointer hover:scale-105 ease-in-out duration-300">
                <h1 >{itm[1].title}</h1>
                <h2 >{itm[1].description}</h2>
                <h3 >{itm[1].where}, {itm[1].time} </h3>
                <h4 ><a href={itm[1].link}>{itm[1].link}</a></h4>
                <br></br>
              </div>
            )
          }
          )
        ) : (<div></div>)}
       </div>
    </div>
  )
}

export default Events