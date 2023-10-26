!constant ORGANISATION_NAME "Organisation"
!constant GROUP_NAME "Group"

workspace {

    model {
    	group $GROUP_NAME {
            user = person "User"
	    softwareSystem = softwareSystem "$ORGANISATION_NAME Software System" {
		webapp = container "Web Application" {
		    user -> this "Uses"
		}
		container "Database" {
		    webapp -> this "Reads from and writes to"
		}
	    }
	}

    }

    views {
        theme default
    }

}
