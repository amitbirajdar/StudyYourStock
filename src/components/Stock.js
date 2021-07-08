import React from 'react';
import Plot from 'react-plotly.js';
import { useLocation } from "react-router-dom";
import './Stock.css';

class Stock extends React.Component {
    constructor(props) {
        super(props);
        //console.log(props.symbol)
        this.state = {
            stockChartXValues : [],
            stockChartYValues : [],
            symbol : props.symbol
        }
    }
    componentDidMount() {
        this.fetchStock();
    }
    fetchStock() {
        const pointerToThis = this;
        //console.log(pointerToThis);
        const API_KEY = 'HGJWFG4N8AQ66ICD';
        let StockSymbol = this.state.symbol;
        let API_CALL = `https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=${StockSymbol}&outputsize=compact&apikey=${API_KEY}`;
        let stockChartXValuesFunction = [];
        let stockChartYValuesFunction = [];

        fetch(API_CALL)
            .then(
                function(response) {
                    return response.json();
                }
            )
            .then(
                function(data) {
                    console.log(data);

                    for (var key in data[`Time Series (Daily)`]) {
                        stockChartXValuesFunction.push(key);
                        stockChartYValuesFunction.push(data[`Time Series (Daily)`][key][`1. open`]);
                    }
                    pointerToThis.setState({
                        stockChartXValues : stockChartXValuesFunction,
                        stockChartYValues : stockChartYValuesFunction
                    });
                }
            )

    }
    render()
    {
        return (
            <div className='stockchart'>
        
            <Plot 
                data = {[
                    {
                        x : this.state.stockChartXValues,
                        y : this.state.stockChartYValues,
                        type : 'scatter',
                        mode : 'lines+markers',
                        marker : { color : 'red'},
                    }
                ]}
                layout={{width: 900, height : 500, title : 'Daily time frame'}}
            />
            </div>
        )
    }
}
export default Stock;