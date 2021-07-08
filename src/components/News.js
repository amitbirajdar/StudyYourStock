import React, { useState,useEffect } from 'react';
import {LandingC} from './LandingC';
import './News.css'

const News = (props) => {
      
    const symbol=props.symbol;
    const [news, setNews] = useState([]);
    const [load1,setLoad1]=useState(false);
    
  
        useEffect(() => {
            fetch("/api/company_news/"+symbol)
                .then((response) => response.json())
                .then((data) => {
                    setNews(data); // new
                    if (data.length > 0){
                        setLoad1(true);
                    }
                });

                
                console.log(news);
        }, [])

  return (
      <div className="NewsDiv">
      <h1 className="RecentNews">RECENT NEWS</h1>
      {
          load1 ? 
            (
                <div className='newsdiv'>{news.map((n)=>(
                <div className='company_news'>
                
                <h2 className="Newstitle">{n.title}</h2>
                <p className='author' >Published by: {n.author}</p>
                    <div className='news_row'>
    
                        <div className='news'>
                            <img src = {n.urlToImage}></img>
                            
                            
                        </div>
                        <div className='news_data'>
                        <p className="publish">{n.publish_date}</p>
                        <p className='urlnews'>{n.url}</p>
                        </div>
                    </div>
                </div>)) } </div>) : 
                <div className='nonews'>No news in the last 30 days!</div>}
    </div>
      );
}

export default News;