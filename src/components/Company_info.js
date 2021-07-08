import React from 'react';
import { Link } from 'react-router-dom';
import {LandingC} from './LandingC';
import "./Company_info.css"

const Company_info = ({symbol,company_name,price,marketcap,image}) => {
    
    const clickHandler = (()=>{
        console.log(symbol);
        
    });

    return (     
        <div className='company_container' >
            <Link to= {{pathname: '/landing',state:  symbol}} style={{textDecoration: 'none'}}>
            <div className='company_row'>
            
                <div className='company'>
                <img src = {image}></img>
                    <p className='symbol' >{symbol}</p>
                    <h1>{company_name}</h1>
                </div>
                <div className='company_data'>
                    <p className="last_price">${price}</p>
                    <p className='marketcap'>MktCap: ${marketcap.toLocaleString()}</p>
            
                </div>
            </div></Link>
        </div>
    );
};
export default Company_info;