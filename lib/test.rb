require 'binance-ruby'
require 'dotenv'
require 'pry'

Dotenv.load

Binance::Api.ping!
binding.pry