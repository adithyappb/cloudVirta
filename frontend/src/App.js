import logo from './logo.svg';
import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import VMManagement from './components/VMManagement';
import ContainerManagement from './components/ContainerManagement';

function App() {
    return (
        <Router>
            <Switch>
                <Route path="/vms" component={VMManagement} />
                <Route path="/containers" component={ContainerManagement} />
            </Switch>
        </Router>
    );
}


export default App;
