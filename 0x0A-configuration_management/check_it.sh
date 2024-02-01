#!/bin/bash

# Specify the path to the util.rb file
UTIL_RB_FILE="/usr/lib/ruby/vendor_ruby/puppet/util.rb"

# Check if the file exists
if [ ! -f "$UTIL_RB_FILE" ]; then
    echo "Error: Puppet util.rb file not found."
    exit 1
fi

# Check if URI.escape is present in the file
if grep -q 'URI.escape' "$UTIL_RB_FILE"; then
    echo "URI.escape method found in $UTIL_RB_FILE."
else
    echo "URI.escape method not found in $UTIL_RB_FILE."
fi

