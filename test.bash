#!/bin/bash
echo "main module"
python -m declarative.main --param hello
echo ""
echo "extended module based on declarative override"
python -m declarative.extended --param hello
echo ""
echo ""
echo "main module for instace based override"
python -m instance.main --param hello
echo ""
echo "extended module based on instace override"
python -m instance.extended --param hello
