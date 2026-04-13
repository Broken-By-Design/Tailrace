package main

import (
	"fmt"
	"resty.dev/v3"
)

func main() {
	client := resty.New()

	type hydro struct {
		FuelType string `json:"fuelType"`
		BmUnit   string `json:"nationalGridBmUnit"`
		Name     string `json:"bmUnitName"`
	}

	var units []hydro

	_, err := client.R().
		SetResult(&units).
		Get("https://data.elexon.co.uk/bmrs/api/v1/reference/bmunits/all")

	if err != nil {
		panic(err)
	}

	hydroTypes := map[string]bool{"NPSHYD": true, "PS": true}

	var filtered []hydro
	for _, u := range units {
		if hydroTypes[u.FuelType] {
			filtered = append(filtered, u)
		}
	}

	for _, u := range filtered {
		fmt.Printf("%-25s  %-8s  %s\n", u.BmUnit, u.FuelType, u.Name)
	}

	fmt.Printf("\ntotal hydro units found: %d\n", len(filtered))
}
