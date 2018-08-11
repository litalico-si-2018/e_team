class CreateArticles < ActiveRecord::Migration[5.2]
  def change
    create_table :articles do |t|
      t.string :articleid
      t.datetime :date
      t.string :body
      t.boolean :isread
      t.string :userid

      t.timestamps
    end
  end
end
