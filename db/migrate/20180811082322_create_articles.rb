class CreateArticles < ActiveRecord::Migration[5.2]
  def change
    create_table :articles do |t|
      t.datetime :date
      t.string :body
      t.boolean :isread

      t.timestamps
    end
  end
end
