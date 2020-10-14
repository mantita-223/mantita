#!/bin/bash

function mantita.return() {
  echo $1
}

function mantitaedit() {
	echo "Launching Mantita Text Edit..."
	python3 ~/mantita/launchmt.py
	echo "[PROCESS COMPLETED]"
}
