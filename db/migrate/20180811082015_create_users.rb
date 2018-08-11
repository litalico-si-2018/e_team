class CreateUsers < ActiveRecord::Migration[5.2]
  def change
    create_table :users do |t|
      t.string :userid
      t.string :name
      t.string :adminid

      t.timestamps
    end
  end
end
