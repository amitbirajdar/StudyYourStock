import React, { Component } from 'react'
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import HomeC from './HomeC';
import {LandingC} from './LandingC';

export default class Main extends Component {
    render() {
        return (
            <BrowserRouter>
            <Switch>
            <Route path="/" exact component={HomeC}/>
            <Route path="/landing" component={LandingC}/>
            </Switch>
            </BrowserRouter>
        )
    }
}

