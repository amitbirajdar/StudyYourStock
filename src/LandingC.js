import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import "./LandingC.css";
import News from './News.js';
import Stock from './Stock';
import Live from './Live';

export const LandingC = (props) => {
  const [data, setData] = useState([]);
  
  const [returns, setReturns] = useState(null);
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());
  const [load1,setLoad1]=useState(false);
  const [len,setLen]=useState(false);
  const [summary, setSummary] = useState([]);
  const location = useLocation();
  const symbol = location.state;

  const url2 = "/api/"+symbol+"/summary";


  function fetchData() {
    console.log("Fetch data function")
    let startDateString = startDate.toISOString().substring(0, 10);
    let endDateString = endDate.toISOString().substring(0, 10);
    const result = fetch(
      "/api/company_data/" +
        symbol +
        "/" +
        startDateString +
        "/" +
        endDateString
    )
      .then((response) => response.json())
      .then((result) => {
        setData((data) => [...result]);
        // console.log(data)
        if(data.length>0){
            calculate();
            console.log(returns)
        }
        else{
          setLen(true);
          console.log('No data present')
          console.log(len);
        }

      });
  }

  const calculate = () => {

    let start_price = 0;
    let end_price = 0;
    let perc = 'null';
    start_price = data[0][1];
    // console.log(data.length-1)
    let lastIndex = data.length - 1;
    end_price = data[lastIndex][1];

    perc = 100 * (end_price - start_price)/(start_price);

    if (perc !== 'null'){
      setReturns(perc.toFixed(2));
      setLoad1(true);
    }
    else{
      setReturns(null)
    }
    console.log(load1);
    

  };

  const getsummary = async () => {

    console.log('Summary data')
    const res = await fetch(url2, {
        headers : { 
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': '*'

          }
    });

    const d = await res.json();
    console.log(d);
    setSummary(d);
};

useEffect(()=>{
   getsummary();
  // console.log(summary);
 }, []);


  return (
    <div className="root">

        <h1 className="header">{symbol}</h1>
        <div className='live'><Live symbol={symbol}/></div>
        <div className="Date">
            <h2 className="returns">CALCULATE RETURN %</h2>
            <div className="startDiv">
                <DatePicker
                  className="startDP"
                  selected={startDate}
                  onChange={(date) => {setStartDate(date);}}
                  dateFormat="yyyy/MM/dd"
                  maxDate={new Date()}
                  isClearable
                  showYearDropdown
                  scrollableMonthYearDropdown
                  placeholderText="Select Start Date"
                />
            </div>
            <div className="endDiv">
                <DatePicker
                  className="endDP"
                  selected={endDate}
                  onChange={(date) => {setEndDate(date)}}
                  dateFormat="yyyy/MM/dd"
                  maxDate={new Date()}
                  isClearable
                  showYearDropdown
                  scrollableMonthYearDropdown
                  placeholderText="Select End Date"
                />
            </div>
            <p className="StockSumm">STOCK SUMMARY</p>
            <div className="summary"> 
                
                <p className="summaryP">Period = {summary[0]} days</p>
                <p className="summaryP">Mean = {summary[1]}</p>
                <p className="summaryP">Minimum = {summary[2]}</p>
                <p className="summaryP">Maximum = {summary[3]}</p>
            </div>
            
            <button
                className="calculate_button"
                id="fetch-button"
                onClick={fetchData}>CALCULATE
            </button>

            {load1 ?
              (<div className="message">
                {returns!=='null' ?
                  (returns < 0 ? <h2 className='red'>Return = {(returns)}%</h2>
                    : <h2 className='green'>Return = {returns}%</h2>)
                  :( <div style={{backgroundColor:"white"}}> {len ? 
                       (<p className='nodata'>No data present for the selected dates</p>):
                       (<p style={{color:"white"}}>No Data</p>)}</div>) } 
            
                      <div> {len ? 
                        (<p className='nodata'></p>):
                        (<p style={{color:"white"}}>No Data</p>)}</div>


            <div className="investment">
                <p style={{color:"black"}}>

                    <span style={{color:"darkblue"}}>$100</span> invested on {startDate.toISOString().substring(0, 10)} would be

                    { (((returns/100)+1)*100) < 100 ?
                      (<span style={{color:"darkred"}}> ${(((returns/100)+1)*100).toFixed(2)}</span>)
                    : (<span style={{color: "darkgreen"}}> ${(((returns/100)+1)*100).toFixed(2)}</span>)}

                    <span style={{color:"black"}}> on {endDate.toISOString().substring(0, 10)}</span>
                </p>
            </div>

            </div>)

            :<div></div>}
        
            <div classname='StockChart'>
            <Stock symbol={symbol}></Stock>
            </div>
            <div><News symbol={symbol}/></div> 
      </div>
    </div>
  );
};
