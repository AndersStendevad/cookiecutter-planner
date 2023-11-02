workspace {
    model {
        user = Person "User" "A user of my software system." {
            tags "Amazon Web Services - User"
        }
        softwareSystem = SoftwareSystem "Software System" "My software system." {
            tags "Amazon Web Services - Category Compute"
        }
        user -> softwareSystem "Uses"
    }

    views {
        systemLandscape {
            include *
            autoLayout lr
        }

        styles {
            element "Element" {
                color #FFFFFF
                shape RoundedBox
                stroke #757575
                metadata false
                description true
            }
            element "Person" {
                color #212121
                background #FFC107

            }
            element "Software System" {
                background #455A64
            }
            element "Container" {
                background #03A9F4
            }
            element "Component" {
                background #00BCD4
            }
        }

        themes https://raw.githubusercontent.com/structurizr/themes/master/amazon-web-services-2023.01.31/icons.json
    }
}
