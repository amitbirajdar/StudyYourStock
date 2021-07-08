import { getByTestId } from '@testing-library/dom';
import React, { useState,useEffect } from 'react';
import './Live.css'


const Live = ({symbol}) => {
    
    console.log(symbol);
    const [count, setCount] = useState(0);
    const [data, setData] = useState([]);
    const url="/api/company";
    const[vari,setvari]=useState('');
    const [lc,setLc] = useState(0);
    const getVari = async () => {
        console.log("Fetching");
        const res = await fetch(url,{
            headers : { 
              'Content-Type': 'application/json',
              'Accept': 'application/json',
              'Access-Control-Allow-Origin': '*'

            }
          });
        const d = await res.json();
        // console.log(d);
        
        for(var i=0; i<d.length; i++){
            if ( d[i][0] == symbol){
                setLc(d[i][2]);
                break;
            };
        };
        setvari(d);
    };

    useEffect(() => {
        



        const interval = setInterval(async () => {
            getVari();
            console.log(lc);
            const res = await fetch(("/api/"+symbol+"/live"), {
                        headers : { 
                            'Content-Type': 'application/json',
                            'Accept': 'application/json',
                            'Access-Control-Allow-Origin': '*'
              
                          }
                    });
                    const d = await res.json();
                    setData(d);
                    //console.log(data);


          setCount(count => count + 1);
        }, 2000);
        return () => clearInterval(interval);
      }, []);

    
    return(
        
        <div className='ticker'>
            {(data[count] < lc) ?
            (<p className = "bt1">${data[count]}</p>)
            : (<p className = "bt2">${data[count]}</p>)
            }
        </div>
            
           
    

    
    );
              


};

export default Live;