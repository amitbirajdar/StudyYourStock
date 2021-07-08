import React,{useState,useEffect} from 'react';
import Company_info from './Company_info';

import "./HomeC.css"
import Stats from './Stats';

function HomeC() {
    const[vari,setvari]=useState('');
    const[search, setSearch] = useState('');
    const[data, setData] = useState([]);
    const[best, setBest] = useState([]);
    const[worst, setWorst] = useState([]);
    const url="/api/company";
    const date='2020-04-26';
    const url1 = "/api/stats/"+date;

       const handleChange = e => {
        setSearch(e.target.value)
    }


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
        console.log(d);

        setvari(d);
    };

    const getstats = async () => {
        const res = await fetch(url1, {
            headers : { 
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Access-Control-Allow-Origin': '*'
  
              }
        });

        const d = await res.json();
        setBest(d[0]);
        setWorst(d[1]);
    };

    useEffect(()=>{
        getVari();
        getstats();
    }, []);

    const filterCompany = Object.values(vari).filter(varis =>
        varis[1].toLowerCase().includes(search.toLowerCase())
        )

    return (
            
        <div className='home'>
            
            <div className='titleheader'><h1 className='titleh1'>STUDY YOUR STOCK</h1></div>
            <div className='search'>
                <div className='stats'>
                    <div className='best'>
                        <div className='header1'>BEST PERFORMERS</div>
                        <div className='header2'>WORST PERFORMERS</div>
                            <table  className='table1'>
                
                            <th>
                                <td className='stockh'>Stock</td>
                                <td className='returnh'>Return %</td>
                            </th>
                            <tr>
                                {
                                    best.map((e)=>(
                                        <tr className='datarow'>
                                            <td className='datarow'>{e[0]}</td>
                                            <td className='returnrow'>{(e[1]).toFixed(2)}</td>
                                        </tr>
                                    ))
                                }
                                {/* <td><p>{best[0][0]}</p></td> */}
                                {/* <td><p className='p1'>{(best[0][1]).toFixed(2)}</p></td> */}
                            </tr>

                            </table>

                            <table  className='table2'>
                
                            <th>
                                <td className='stockh'>Stock</td>
                                <td className='returnh'>Return %</td>
                            </th>
                            <tr>
                                {
                                    worst.map((e)=>(
                                        <tr>
                                            <td className='datarow'>{e[0]}</td>
                                            <td className='returnrow'>{(e[1]).toFixed(2)}</td>
                                        </tr>
                                    ))
                                }
                            </tr>

                            </table>
                
            </div>
                    
                </div>
                <h1 className='text'>SEARCH COMPANY</h1>
                <form >
                    <input type='text' placeholder='Enter Company Name' className='input' onChange={handleChange}></input>
                </form>
                
            <div className="data">
                
                {filterCompany.map(vari => {
                    return (
                        <Company_info 
                        symbol={vari[0]} 
                        company_name={vari[1]} 
                        price={vari[2]} 
                        marketcap={vari[3]} 
                        image={vari[5]}/>
                )
                })}
            </div>
            
            </div>
        </div>
        
    )
}

export default HomeC;
