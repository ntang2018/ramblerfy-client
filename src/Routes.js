import React from "react";
import { Route, Switch } from "react-router-dom";
import Home from "./containers/Home";
import NfError from "./containers/NfError";

export default function Routes() {
  return (
    <Switch>

      <Route path="/" exact component={Home} />

      { /* Redirects to 404 error for any route that doesnt match */ }
      <Route component={NfError}/>
    </Switch>
  );
}
