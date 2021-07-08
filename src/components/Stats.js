import { getByTestId } from '@testing-library/dom';
import React, { useState,useEffect } from 'react';
import './Stats.css'

const Stats = () => {
      
    // const [data, setData] = useState([]);
    // const [best, setBest] = useState([]);
    // const [worst, setWorst] = useState([]);
    // let database = null;
    // const date = '2020-04-26';
    // useEffect(() => {
    //     fetch("/api/stats/"+date)
    //         .then((response) => response.json())
    //         .then((data) => {
    //             setData(data);
    //         });
    //         database = data;
    //         setBest(data[0]);
    //         setWorst(data[1]); // new
    //         console.log(data);
            
    // }, []);

    return(
              
        <div></div>

        // <div className='stats'>
        //     <div className='best'>
        //         <div className='header1'>getByTestId</div>
        //         <table  className='table1'>
                
        //         <th>
        //             <td className='stockh'>Stock</td>
        //             <td className='returnh'>Return %</td>
        //         </th>
        //         <tr>
        //             <td><p>{data[0][0][0]}</p></td>
        //             <td><p className='p1'>{(data[0][0][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[0][1][0]}</p></td>
        //             <td><p className='p1'>{(data[0][1][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[0][2][0]}</p></td>
        //             <td><p className='p1'>{(data[0][2][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[0][3][0]}</p></td>
        //             <td><p className='p1'>{(data[0][3][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[0][4][0]}</p></td>
        //             <td><p className='p1'>{(data[0][4][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[0][5][0]}</p></td>
        //             <td><p className='p1'>{(data[0][5][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[0][6][0]}</p></td>
        //             <td><p className='p1'>{(data[0][6][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[0][7][0]}</p></td>
        //             <td><p className='p1'>{(data[0][7][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[0][8][0]}</p></td>
        //             <td><p className='p1'>{(data[0][8][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[0][9][0]}</p></td>
        //             <td><p className='p1'>{(data[0][9][1]).toFixed(2)}</p></td>
        //         </tr>
        //         </table>
        //     </div> 
        //     <div className='worst'>
        //     <div className='header1'>getByTestId</div>
        //     <table  className='table2'>
        //         <th>
        //             <td className='stockh'>Stock</td>
        //             <td className='returnh'>Return %</td>
        //         </th>
        //         <tr>
        //             <td><p>{data[1][0][0]}</p></td>
        //             <td><p className='p1'>{(data[1][0][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[1][1][0]}</p></td>
        //             <td><p className='p1'>{(data[1][1][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[1][2][0]}</p></td>
        //             <td><p className='p1'>{(data[1][2][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[1][3][0]}</p></td>
        //             <td><p className='p1'>{(data[1][3][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[1][4][0]}</p></td>
        //             <td><p className='p1'>{(data[1][4][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[1][5][0]}</p></td>
        //             <td><p className='p1'>{(data[1][5][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[1][6][0]}</p></td>
        //             <td><p className='p1'>{(data[1][6][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[1][7][0]}</p></td>
        //             <td><p className='p1'>{(data[1][7][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[1][8][0]}</p></td>
        //             <td><p className='p1'>{(data[1][8][1]).toFixed(2)}</p></td>
        //         </tr>
        //         <tr>
        //         <td><p>{data[1][9][0]}</p></td>
        //             <td><p className='p1'>{(data[1][9][1]).toFixed(2)}</p></td>
        //         </tr>
        //         </table>
                
        //     </div>
            
            
        // </div>     
    );
}

export default Stats;