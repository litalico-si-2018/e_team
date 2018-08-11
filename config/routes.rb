Rails.application.routes.draw do
  get '/users/:name/articles', to: 'articles#show'
  get '/users/:name/articles/:date', to: 'articles#show'
  get '/users/:name/admin/articles', to: 'articles#show'
  get '/users/:name/admin/articles/:date', to: 'articles#show'
  get '/admins/:name', to: 'users#index'
  resources :articles
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root 'application#hello'
  
end
