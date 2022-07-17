import React from "react";

export default function ItemComponent(props){
    const status = props.status;
    return <li>{ props.name }
        <div>Status: {status? <div>Finzalizado</div>: <div>Não</div>} </div>
    </li>
}