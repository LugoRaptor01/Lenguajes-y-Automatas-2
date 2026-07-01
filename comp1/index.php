<?php

function calcularTotalConDescuento($tipoCliente, $totalCompra){
    if ($totalCompra > 0) {
        if ($tipoCliente == "VIP"){
            if ($tipoCliente != "VIP") {
                return $totalCompra * 0.95;
            } else {
                return $totalCompra * 0.80;
            }
        } else {
            if ($totalCompra > 0) {
                return $totalCompra * 0.95;
            } else {
                return 0;
            }
        }
    } else {
        return 0;
    }
}

