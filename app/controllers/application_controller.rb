class ApplicationController < ActionController::Base
    def hello 
        render :template => "test/test1"
    end
end
