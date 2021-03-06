<script>
// Note the data/props/computed setup as per https://vuejs.org/v2/guide/components.html
// Props are passed down from root; but we need to cast them into data
// so that it can then mutate them here in response to children
import AjaxMixin from '../ajax/AjaxMixin.vue'
import UnallocatedItemsContainer from '../containers/UnallocatedItemsContainer.vue'
import DrawHeader from '../draw/DrawHeader.vue'
import Debate from '../draw/Debate.vue'
import AutoSaveCounter from '../draganddrops/AutoSaveCounter.vue'
import DroppableGeneric from '../draganddrops/DroppableGeneric.vue'
import SlideOverContainerMixin from '../../info/SlideOverContainerMixin.vue'
import SlideOver from '../../info/SlideOver.vue'
import SortableTableMixin from '../../tables/SortableTableMixin.vue'
import _ from 'lodash'

export default {
  mixins: [AjaxMixin, SlideOverContainerMixin, SortableTableMixin],
  components: {
    DrawHeader, AutoSaveCounter, Debate,
    DroppableGeneric, UnallocatedItemsContainer, SlideOver
  },
  data: function () {
    return {
      debates: this.initialDebates,
      unallocatedItems: this.initialUnallocatedItems,
      headers: [
        {'key':'bracket'},{'key':'liveness'},{'key':'importance'},
        {'key':'venue'},
        {'key':'affirmative'},{'key':'negative'},
        {'key':'og'},{'key':'oo'},{'key':'cg'},{'key':'co'},
        // Team positions
      ]
    }
  },
  props: ['initialDebates', 'initialUnallocatedItems', 'roundInfo'],
  created: function () {
    // Watch for events on the global event hub
    this.$eventHub.$on('unassign-draggable', this.moveToUnused)
    this.$eventHub.$on('assign-draggable', this.moveToDebate)
    this.$eventHub.$on('update-allocation', this.updateDebates)
    this.$eventHub.$on('update-unallocated', this.updateUnallocatedItems)
  },
  computed: {
    sortableData: function() {
      return this.debates // Enables SortableTableMixin
    },
    teams: function() {
      // Return all teams (in debates) as a single array
      var allTeams = _.map(this.debates, function(debate) {
        return _.values(debate.teams)
      })
      return _.flattenDeep(allTeams)
    },
    adjudicators: function() {
      // Return all adjs (in debates) as a single array
      var allPanellists = _.map(this.debates, function(debate) {
        return _.map(debate.panel, function(panel) {
          return panel.adjudicator
        })
      })
      return _.flattenDeep(allPanellists)
    },
    venues: function() {
      // Return all teams as a single array
      var allVenues = _.map(this.debates, function(debate) {
        return debate.venue
      })
      return allVenues
    },
    debatesById: function() {
      return _.keyBy(this.debates, 'id')
    },
    teamsById: function() {
      return _.keyBy(this.teams, 'id')
    },
    adjudicatorsById: function() {
      return _.keyBy(this.adjudicators, 'id')
    },
    institutionsById: function() {
      var teamInstitutions = _.map(this.teams, function(team) {
        return team.institution
      })
      var adjInstitutions = _.map(this.adjudicators, function(adjudicator) {
        return adjudicator.institution
      })
      var uniqueInstitutions = _.uniq(teamInstitutions.concat(adjInstitutions))
      return _.keyBy(uniqueInstitutions, 'id')
    },
    unallocatedById: function() {
      return _.keyBy(this.unallocatedItems, 'id')
    },
    positions: function() {
      return this.debates[0].positions // Shortcut function
    }
  },
  methods: {
    updateDebates: function(updatedDebates) {
      this.debates = updatedDebates // Match internal data to json response
    },
    updateUnallocatedItems: function(updatedUnallocatedItems) {
      this.unallocatedItems = updatedUnallocatedItems // As above
    },
    // Duplicating sortableHeaderMixin; but can't inheret in a slot
    sortClasses: function(key) {
      var baseCSS = "glyphicon vue-sort-key "
      if (this.sortKey === key) {
        if (this.sortOrder === "asc") {
          return baseCSS + "text-success glyphicon-sort-by-attributes-alt"
        } else {
          return baseCSS + "text-success glyphicon-sort-by-attributes"
        }
      }
      return baseCSS + "text-muted glyphicon-sort"
    },
    getSortableProperty(row, orderedHeaderIndex) {
      // Rather than an array of cells (as in Table) row is a Debate
      // So just return the relevant property
      if (typeof row[this.sortKey] === 'string' ||
          typeof row[this.sortKey] === 'number') {
        return row[this.sortKey]
      } else if (this.sortKey === 'venue') {
        if (!_.isNull(row.venue)) {
          return row.venue.name
        } else {
          return "" // Venues can be null
        }
      } else if (_.includes(["affirmative", "negative"], this.sortKey)) {
        if (!_.isUndefined(row.teams[this.sortKey])) {
          return row.teams[this.sortKey].short_name
        } else {
          return ""  // Teams in a position can be null
        }
      }
      console.log('Couldnt find sorting property')
    }
  }
}
</script>
