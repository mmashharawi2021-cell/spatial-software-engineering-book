const states = ["loading","ready","empty","error"] as const;
type ViewState = typeof states[number];
function canShowMap(s: ViewState){ return s === "ready" || s === "empty"; }
